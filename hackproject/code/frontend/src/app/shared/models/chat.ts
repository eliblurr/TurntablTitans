export interface Message {
  type: string;
  message: string;
}

export interface Chat {
  chatId: string
  chatName: string
}

export interface ChatRequest {
  prompt: ChatPrompt
  chat_id: string
}

export interface ComputerAnswer {
  id: string,
  value: string,
  order: number
}

export interface ChatPrompt {
  body: string,
  native_language: string
}

export interface ChatResponse {
  prompt: string
  response: string
}
