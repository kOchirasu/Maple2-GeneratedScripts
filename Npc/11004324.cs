using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004324: Lennon
/// </summary>
public class _11004324 : NpcScript {
    internal _11004324(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011492$ 
                // - What is she thinking?!
                return true;
            case 10:
                // $script:1010140307011493$ 
                // - Sigh. Once $npcName:11004323[gender:1]$ sets her mind to something, there's little hope of changing it.
                switch (selection) {
                    // $script:1010140307011494$
                    // - What's the matter?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:1010140307011495$ 
                // - Oh, $MyPCName$. Fancy meeting you here.
                // $script:1010140307011496$ 
                // - After not seeing $npcName:11004323[gender:1]$ for a few days I got worried. I asked around and found out she came here all alone. So, I dropped everything and followed her here.
                // $script:1010140307011497$ 
                // - I asked her what's going on, but she won't tell me anything. Maybe she doesn't think she can depend on me...
                // $script:1010140307011498$ 
                // - In any case, this is no place for her to be running off to alone! She needs to go home.
                switch (selection) {
                    // $script:0111232407012693$
                    // - That seems like a conversation you should have with her.
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0111232407012694$ 
                // - I've tried! Maybe you can talk some sense into her?
                return true;
            case 30:
                // $script:0109125407012659$ 
                // - I'm worried...
                // $script:0109125407012660$ 
                // - How can I get $npcName:11004323[gender:1]$ to change her mind? We should be in Victoria Island, not here!
                return true;
            default:
                return true;
        }
    }
}
