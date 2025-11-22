from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from tienda.models import Producto

def obtener_carrito(request):
    carrito = request.session.get("carrito", {})
    if isinstance(carrito, list):
        carrito = {}
        request.session["carrito"] = carrito
    return carrito


def ver_carrito(request):
    carrito = obtener_carrito(request)
    productos = []
    total = 0

    for id_str, datos in carrito.items():
        producto = get_object_or_404(Producto, id=int(id_str))
        subtotal = datos["cantidad"] * producto.precio
        total += subtotal

        productos.append({
            "producto": producto,
            "cantidad": datos["cantidad"],
            "subtotal": subtotal,
        })

    return render(request, "carrito/carrito.html", {
        "productos": productos,
        "total": total,
    })


def agregar_carrito(request, producto_id):
    carrito = obtener_carrito(request)
    id_str = str(producto_id)
    cantidad = int(request.POST.get("cantidad", 1))

    if id_str in carrito:
        carrito[id_str]["cantidad"] += cantidad
    else:
        carrito[id_str] = {"cantidad": cantidad}

    request.session["carrito"] = carrito
    request.session.modified = True
    return redirect("carrito:carrito")


def restar_carrito(request, producto_id):
    carrito = obtener_carrito(request)
    id_str = str(producto_id)

    if id_str in carrito:
        carrito[id_str]["cantidad"] -= 1
        if carrito[id_str]["cantidad"] <= 0:
            del carrito[id_str]

    request.session["carrito"] = carrito
    request.session.modified = True
    return redirect("carrito:carrito")


def eliminar_carrito(request, producto_id):
    carrito = obtener_carrito(request)
    id_str = str(producto_id)

    if id_str in carrito:
        del carrito[id_str]

    request.session["carrito"] = carrito
    request.session.modified = True
    return redirect("carrito:carrito")


def limpiar_carrito(request):
    request.session["carrito"] = {}
    request.session.modified = True
    return redirect("carrito:carrito")


def finalizar_compra(request):
    carrito = obtener_carrito(request)
    productos = []
    total = 0

    for id_str, datos in carrito.items():
        producto = get_object_or_404(Producto, id=int(id_str))
        subtotal = datos["cantidad"] * producto.precio
        total += subtotal

        productos.append({
            "producto": producto,
            "cantidad": datos["cantidad"],
            "subtotal": subtotal,
        })

    # ---- Generar HTML dinámico ----
    tabla = ""
    for item in productos:
        tabla += f"""
        <tr>
            <td>{item['producto'].nombre}</td>
            <td>{item['cantidad']}</td>
            <td>${item['producto'].precio}</td>
            <td><strong>${item['subtotal']}</strong></td>
        </tr>
        """

    html_message = f"""
    <h2 style='color:#0d6efd;'>Gracias por tu compra 🛍</h2>
    <p>Tu pedido se procesará en las próximas 24 horas.</p>

    <h3>Resumen del pedido:</h3>
    <table border='1' cellspacing='0' cellpadding='8'>
        <tr>
            <th>Producto</th>
            <th>Cantidad</th>
            <th>Precio Unidad</th>
            <th>Subtotal</th>
        </tr>
        {tabla}
    </table>

    <h3>Total pagado: <strong>${total}</strong></h3>
    <br>
    <p>Gracias por confiar en <strong>Genesis Clothing</strong>.</p>
    """

    try:
        send_mail(
            subject="Confirmación de compra 🛒",
            message="Gracias por tu compra",   # respaldo si no soporta HTML
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email],
            html_message=html_message,
            fail_silently=False
        )
        messages.success(request, "Compra realizada con éxito. Revisa tu correo ✔")
    except Exception as e:
        print("ERROR EN ENVÍO:", e)
        messages.error(request, "Hubo un problema enviando el correo.")

    request.session["carrito"] = {}
    return redirect("carrito:carrito")





