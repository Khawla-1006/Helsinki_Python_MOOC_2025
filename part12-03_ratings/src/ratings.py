# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def order_ratings(item : dict):
        return item["rating"]
    
    return sorted(items,key=order_ratings,reverse=True)