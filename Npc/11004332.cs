using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004332: Lanemone
/// </summary>
public class _11004332 : NpcScript {
    internal _11004332(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1102172107011635$ 
                // - Hm...
                return true;
            case 20:
                // $script:1010140307011563$ 
                // - Mm?
                return true;
            case 10:
                // $script:1102172107011636$ 
                // - I sense something powerful. Something... wrong.
                return true;
            case 30:
                // $script:1010140307011564$ 
                // - Hey, you!
                // $script:1010140307011565$ 
                // - Long time no see.
                // $script:1010140307011566$ 
                // - I wasn't expecting to run into you here.
                switch (selection) {
                    // $script:1010140307011567$
                    // - What brings you here?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:1010140307011568$ 
                // - Well, that geezer—erm, Mr. $npcName:11004233[gender:0]$ sent me here.
                // $script:1010140307011569$ 
                // - The Frontier Foundation caught wind of something quite unexpected here on this continent that warranted investigation.
                // $script:1010140307011570$ 
                // - Traces of lapenta energy!
                // $script:1010140307011571$ 
                // - But I suppose you already knew that.
                // $script:1010140307011572$ 
                // - You should be careful. There's no telling what kinds of dangers lurk in this land.
                switch (selection) {
                    // $script:0111232407012699$
                    // - You too. Take care of yourself.
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:0111232407012700$ 
                // - Oh, you don't have to worry about me.
                return true;
            default:
                return true;
        }
    }
}
