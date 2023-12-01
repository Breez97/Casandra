#Очищение окна
def clear_packs(packs):
    if len(packs) != 0:
        for i in range(0, len(packs)):
            packs[i].pack_forget()
        packs.clear()