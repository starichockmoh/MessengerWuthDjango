import styled from "styled-components";
import {CheckOutlined} from "@ant-design/icons";

type MessageBlockType = {
    IsFriend: boolean
    color: string
}

export const MessageBlock = styled("div")`
  margin: 10px;
  display: flex;
  flex-direction: column;
  

  div {
    align-self: ${(props: MessageBlockType) => props.IsFriend ? 'flex-start' : 'flex-end'};
    border-radius: 5px;
    padding: 5px;
    word-break: break-word;
    background:  ${(props: MessageBlockType) => props.color};
    display: flex;
    align-items: baseline;
    
  }
`

export const MessageInfo = styled.div`
  max-width: 30vw;
  display: flex;
  flex-direction: column;
`
export const MessageData = styled.div`
  color: #CDC5BF;
`

//icons
export const TickIcon = styled(CheckOutlined)`
  font-size: 14px;
  color: #08c;
  margin-left: 5px;
`