# Criando cadastro do funcionario com dicionário composto

funcionarios = {
     "44356":{
             "nome":"Vitor Davi",
             "telefone":"1191212135",
             "data_nascimento":"10/12/2010",
             "cargo":"Jovem Aprendiz",
             "habilidades": ["front-end","java","python"]
    },
     "42568":{
            "nome":"Adriano Barros",
            "telefone":"11940404040",
            "data_nascimento":"24/03/2010",
            "cargo":"Jovem Aprendiz",
            "habilidades": ["front-end","java","python"]
     },
     "41548":{
            "nome":"Mimi Cristine",
            "telefone":"11970707070",
            "data_nascimento":"15/09/2010",
            "cargo":"Jovem Aprendiz",
            "habilidades": ["office","python"]
     }

}

print(funcionarios["44356"]["habilidades"][1])