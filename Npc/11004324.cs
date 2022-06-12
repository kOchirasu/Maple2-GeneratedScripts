using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004324: Lennon
/// </summary>
public class _11004324 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    // Select 0:
    // $script:1010140307011492$
    // - What is she thinking?!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1010140307011493$
                // - Sigh. Once $npcName:11004323[gender:1]$ sets her mind to something, there's little hope of changing it.
                switch (selection) {
                    // $script:1010140307011494$
                    // - What's the matter?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:1010140307011495$
                // - Oh, $MyPCName$. Fancy meeting you here.
                return 20;
            case (20, 1):
                // $script:1010140307011496$
                // - After not seeing $npcName:11004323[gender:1]$ for a few days I got worried. I asked around and found out she came here all alone. So, I dropped everything and followed her here.
                return 20;
            case (20, 2):
                // $script:1010140307011497$
                // - I asked her what's going on, but she won't tell me anything. Maybe she doesn't think she can depend on me...
                return 20;
            case (20, 3):
                // $script:1010140307011498$
                // - In any case, this is no place for her to be running off to alone! She needs to go home.
                switch (selection) {
                    // $script:0111232407012693$
                    // - That seems like a conversation you should have with her.
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0111232407012694$
                // - I've tried! Maybe you can talk some sense into her?
                return -1;
            case (30, 0):
                // $script:0109125407012659$
                // - I'm worried...
                return 30;
            case (30, 1):
                // $script:0109125407012660$
                // - How can I get $npcName:11004323[gender:1]$ to change her mind? We should be in Victoria Island, not here!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Next,
            (20, 2) => NpcTalkButton.Next,
            (20, 3) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
