class Request:
    def __init__(self, request):

        req_list = request.split()
        count = 0

        for i in req_list:
            count += 1
            if i in ['из', 'с', 'со']:
                break

        amount = req_list[count - 3]
        product = req_list[count - 2]
        from_str = req_list[count]
        to_str = req_list[count + 2]

        self.from_str = from_str
        self.to_str = to_str
        self.amount = int(amount)
        self.product = product
