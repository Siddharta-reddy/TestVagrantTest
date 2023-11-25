
class Cart :
    def MaxGST(self) :
        prd=''
        max_gst = 0 
        for i in Basket :
            if max_gst < (i[0]*i[2]*i[1])/100 :
                max_gst= (i[0]*i[2]*i[1])/100
                prd=i
        print('The product for  which we paid maximum GST amount is :', end=' ')
        for i in range(len(Basket)) :
            if prd==Basket[i] :
                print(b[i])
    def TotalPaid(self) :
        total = 0
        for i in Basket :
            if i[0]>=500 :
                total = total + ((i[0]*i[2])*0.95 + ((i[0]*i[2])*i[1]/100))
            else :
                total = total + ((i[0]*i[2]) + ((i[0]*i[2])*i[1]/100))
        print('Total amount to be paid to the shop-keeper is : ', + total)
cart = Cart
Leather_wallet = [1100, 18, 1]
Umbrella = [900, 12, 4]
Cigarette = [200, 28, 3]
Honey = [100, 0, 2]
b=['Leather_wallet', 'Umbrella', 'Cigarette', 'Honey']
Basket= [Leather_wallet, Umbrella, Cigarette, Honey]
cart.MaxGST(b)
cart.TotalPaid(b)