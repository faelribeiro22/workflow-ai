import json

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_x_post(topic: str) -> str:
    with open("post-examples.json", "r") as f:
        examples = json.load(f)

    examples_str = ""
    for i, example in enumerate(examples, 1):
        examples_str += f"""
        <example-{i}>
            <topic>
                {example['topic']}
            </topic>
            <post>
                {example['post']}
            </post>
        </example-{i}>
        """

    prompt = f"""
        Você é um expert em mídias sociais, especialmente no Twitter (X).

        Sua tarefa é gerar um post para o Twitter (X) com base na entrada do usuário.
        O post deve ser curto, direto e engajador, com no máximo 280 caracteres.

        Mantenha o tom amigável e profissional, evitando jargões técnicos desnecessários.

        Aqui está a entrada do usuário:
        <topic>
        {topic}
        <topic>

        Aqui está alguns exemplos de posts que você pode usar como referência:
        <examples>
            {examples_str}
        </examples>

        Por favor use o ton, linguagem, estrutura e estilos dos exemplos acima para gerar um post que seja engajador e relevante para o tópico fornecido pelo usuário. Não use o contexto dos exemplos!
"""
    response = client.responses.create(
        model="gpt-4o",
        input=prompt,
    )

    return response.output_text


def main():
    # user input => AI (LLM) to generate X post => output post
    
    usr_input = input("What should the post be about? ")
    x_post = generate_x_post(usr_input)
    print("Generated X post:")
    print(x_post)




if __name__ == "__main__":
    main()
