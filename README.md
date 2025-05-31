# IPS


# 🖼️ Image Processing Service - FastAPI

Um serviço backend completo para **upload, transformação e recuperação de imagens** em tempo real, no estilo do Cloudinary — com autenticação JWT, salvamento local e pronto para expansão com S3, Redis, Celery, etc.

---

## 🚀 Funcionalidades

- Registro e login de usuários com JWT
- Upload de imagens (local)
- Transformações aplicáveis:
  - Redimensionamento
  - Recorte (crop)
  - Rotação
  - Flip (espelhamento)
  - Grayscale / Sepia / Blur / Sharpen
  - Compressão
  - Watermark com texto
  - Conversão de formato (PNG, JPEG, WEBP)
- Listagem de imagens por usuário
- Rate limit por IP (10 requisições/minuto)
- Swagger UI para testes interativos

---

## 🛠️ Tecnologias usadas

- Python 3.10+
- FastAPI + Uvicorn
- JWT (python-jose)
- Pillow (PIL)
- SlowAPI (rate limit)
- dotenv
- `python-multipart` (upload)

---

## ⚙️ Como rodar localmente

### 1. Clone o projeto e instale as dependências

``bash
git clone https://github.com/seu-usuario/image-processing-service.git
cd image-processing-service

pip install -r requirements.txt

2. Crie o arquivo .env (mesmo usando local)

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
S3_BUCKET_NAME=

3. uvicorn main:app --reload

4. Acesse a documentação
📌 Swagger: http://127.0.0.1:8000/docs

🧪 Fluxo de uso no Swagger
/auth/register → Registra novo usuário

/auth/token → Faz login e obtém token JWT

Clique em Authorize e cole o token: Bearer <seu_token>

/images → Upload de imagem

/images/{filename}/transform → Aplica transformações

/images → Lista imagens do usuário

/images/{filename} → Baixa a imagem original ou transformada

🧰 Próximas melhorias
Upload para AWS S3 (já parcialmente implementado)

Cache inteligente de transformações

Fila de processamento com Celery + Redis

Paginação nos endpoints de listagem

Watermark com imagem (além de texto)

👨‍💻 Autor
Torres — Projeto criado para estudo de backend moderno com Python FastAPI.

