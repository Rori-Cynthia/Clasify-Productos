class Product():
    def __init__(self, input_code, input_weight, input_fragility):
        self.code = input_code
        self.weight = int(input_weight)
        self.fragility = input_fragility

    products_code = {
        "A": "Productos Alimenticios",
        "B": "Productos Electrónicos",
        "C": "Otros Productos",
    }
    
    products_fragility = {
        "F": "Fragil",
        "N": "No fragil",
    }

    def evaluate_input(self):    
        if self.code not in self.products_code or self.fragility not in self.products_fragility:
            print("--- Ha ingresado al menos un dato inválido, intentelo de nuevo ---")
            show_prompt()

    def evaluate_code(self):
        if self.code in self.products_code:
            self.code = self.products_code[self.code]

    def evaluate_weight(self):
        if self.weight < 10:
            self.weight = "Ligero"
        elif self.weight >= 10 and self.weight < 20:
            self.weight = "Mediano"
        else:
            self.weight = "Pesado"

    def evaluate_fragility(self):
        if self.fragility in self.products_fragility:
            self.fragility = self.products_fragility[self.fragility]

    def evaluate_product(self):
        print("---")
        if self.code == "Productos Alimenticios":
            if self.weight == "Pesado" and self.fragility == "Fragil":
                print("Producto alimenticio pesado y frágil: Manejar con extremo cuidado");
            elif self.weight == "Mediano" and self.fragility == "Fragil":
                print("Producto alimenticio mediano y frágil: Manejar con cuidado")
            elif self.weight == "Ligero":
                print("Producto alimenticio ligero: Manejar con cuidado estándar")

        if self.code == "Productos Electrónicos":
            if self.fragility == "Fragil":
                print("Producto electrónico frágil: Manejar con cuidado")
            elif self.fragility != "Fragil" and self.weight == "Pesado":
                print("Producto electrónico no frágil: Manejo estándar")
            elif self.fragility != "Fragil" and (self.weight == "Mediano" or self.weight == "Ligero"):
                    print("Producto electrónico no frágil: Manejo estándar")
    
        if self.code == "Otros productos":
            if self.weight == "Pesado" and self.fragility == "Fragil":
                print("Producto pesado y frágil: Manejar con precaución adicional")
            elif self.weight == "Pesado" and self.fragility != "Fragil":
                print("Producto pesado y no frágil: Manejo estándar")
            elif self.weight == "Pesado" or self.weight == "Ligero":
                print("Producto no pesado: Manejo estándar")
        print("---")

def run_functions(input_code, input_weight, input_fragility):
    new_product = Product(input_code, input_weight, input_fragility)
    new_product.evaluate_input()
    new_product.evaluate_code()
    new_product.evaluate_weight()
    new_product.evaluate_fragility()
    new_product.evaluate_product()

def show_prompt():
    try:
        input_code = input('Indique el codigo del producto. Puede ser:\n"A" para productos alimenticios\n"B" para productos electrónicos y\n"C" para otros productos: ')
        input_weight = int(input("Ingrese el peso de su producto: "))
        input_fragility = input('Indique si su producto es fragil o no: "F"" para fragil y "N" para no fragil: ')
        run_functions(input_code, input_weight, input_fragility)
    except Exception:
        print("Ingresó un dato invalido")
        show_prompt()

def run ():
    show_prompt()

if __name__ == "__main__":
    run()