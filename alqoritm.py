
def yerləri_təyin_et(xallar):
    xallar_ve_indekslər = list(enumerate(xallar))
    sıralanmış_xallar = sorted(xallar_ve_indekslər, key=lambda x: x[1], reverse=True)
    
    # Yerləri təyin etmək üçün boş bir siyahı yaradırıq
    yerlər = [0] * len(xallar)
    for sıralama, (indeks, xal) in enumerate(sıralanmış_xallar, start=1):
        yerlər[indeks] = f"{sıralama}-ci"
    
    return yerlər

xallar = [5, 3, 4, 2, 1]
yerlər = yerləri_təyin_et(xallar)
print(yerlər)
