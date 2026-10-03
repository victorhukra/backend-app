from models.usuario import listar_usuarios, buscar_usuario_por_id


def obter_usuarios(nome="", pagina=1):
    return listar_usuarios(nome, pagina)


def obter_perfil_usuario(id):
    return buscar_usuario_por_id(id)