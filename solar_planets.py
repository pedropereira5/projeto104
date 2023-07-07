import cv2

# Ler a imagem do arquivo
img = cv2.imread("solar-system.jpg")

# Adicionar texto abaixo de cada planeta
cv2.putText(img, "Mercury", (170, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Venus", (280, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Earth", (380, 430), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Mars", (480, 580), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Jupiter", (550, 700), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Saturn", (650, 780), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Uranus", (730, 820), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.putText(img, "Neptune", (800, 840), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Exibir a imagem com os nomes dos planetas
cv2.imshow("Resultado", img)
cv2.waitKey(0)

# Salvar a imagem final
cv2.imwrite("Solar_system_with_names.jpg", img)
