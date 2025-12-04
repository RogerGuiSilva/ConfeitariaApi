from flask import jsonify


itens = [
    {
        "id": 1,
        "nome": "Sãobolo",
        "descricao": "Bolo do São Paulo",
        "preco": 49.99,
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUgm5a7_Mnbi2oxJvWg_ul2R5Foed7FD0BvA&s"
    },
    {
        "id": 2,
        "nome": "Bolo Ceni",
        "descricao": "Bolo em homenagem ao Idolo",
        "preco": 59.90,
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeWQoa-Uju9_liiRcqoYrmutG_UbccdnEOoA&s"
    },
    {
        "id": 3,
        "nome": "Bolo Tricolor",
        "descricao": "Bolo dos Campeões",
        "preco": 30.30,
        "foto": "https://aninhamiranda.wordpress.com/wp-content/uploads/2013/06/4.jpg"
    }
]

itens_por_id = {item["id"]: item for item in itens}

def buscar_cardapio():
    return jsonify(itens)

def buscar_por_id(item_id):
    item = itens_por_id.get(item_id)
    if item is None:
        return jsonify({"erro": "Item não encontrado"}), 404
    return jsonify(item)
