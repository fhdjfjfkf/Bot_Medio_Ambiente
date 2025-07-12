import discord

reciclables = {
    "botella": "se recicla en el contenedor amarillo",
    "metal": "se recicla en el contenedor amarillo",
    "cajas": "se recicla en el contenedor azul",
    "vidrio": "se recicla en el contenedor verde",
    "desechos": "se recicla en el contenedor negro",
    "cascaras de frutas": "se recicla en el contenedor marrón",
    "Tapas plásticas": "se recicla en el contenedor amarillo",
    "papel": "se recicla en el contenedor azul",
    "cartón": "se recicla en el contenedor azul",
    "lata": "se recicla en el contenedor amarillo",
    "brik": "se recicla en el contenedor amarillo",
    "ropa": "no va al tacho, se dona o va al punto limpio",
    "pilas": "no va al tacho, se lleva a un punto limpio especial",
    "juguete roto": "va al contenedor negro o punto limpio",
    "madera tratada": "no se recicla, llevar a un punto limpio",
    "papel aluminio": "se recicla en el contenedor amarillo (si está limpio)",
    "revistas": "se recicla en el contenedor azul",
    "periódico": "se recicla en el contenedor azul",
    "botella de vidrio": "se recicla en el contenedor verde",
    "tetrapak": "se recicla en el contenedor amarillo",
    "bolsa plástica": "se recicla en el contenedor amarillo (si está limpia)",
    "bandeja de aluminio": "se recicla en el contenedor amarillo (si está limpia)",
    "CDs/DVDs": "no se reciclan en casa, llévalos a un punto limpio",
    "focos": "no van al tacho, punto limpio especial",
    "termómetros": "no van al tacho, residuos peligrosos",
    "aserrín": "se puede compostar si es natural (contenedor marrón)",
    "cepillo de dientes": "contenedor negro o punto limpio",
    "pañuelo de papel usado": "contenedor negro",
    "latas de conserva": "se reciclan en el contenedor amarillo",
    "tetrabrik": "se recicla en el contenedor amarillo",

}

def setup(bot):
    @bot.command()
    async def test(ctx, *args):
        respuesta = ' '.join(args)
        await ctx.send(respuesta)

    @bot.command()
    async def Reciclables(ctx, *args):
        input = ' '.join(args)
        for item,descripccion in reciclables.items ():
            if(input.lower() == item.lower()):
                await ctx.send(descripccion)
        
        await ctx.send("El objeto no se encuentra en la lista de reciclables")
