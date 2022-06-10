using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004322: Startz
/// </summary>
public class _11004322 : NpcScript {
    internal _11004322(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1102172107011627$ 
                // - Hm...
                return true;
            case 20:
                // $script:1010140307011471$ 
                // - Hm...
                return true;
            case 10:
                // $script:1102172107011628$ 
                // - That might look good on my menu...
                return true;
            case 30:
                // $script:1010140307011472$ 
                // - Hmm?
                switch (selection) {
                    // $script:1010140307011473$
                    // - Good to see you! It's been a while.
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:1010140307011474$ 
                // - Yeah, whatever.
                switch (selection) {
                    // $script:1010140307011475$
                    // - What are you doing here?
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:1010140307011476$ 
                // - $npcName:11004319[gender:1]$ dragged us here to search for dark dragons.
                switch (selection) {
                    // $script:1010140307011477$
                    // - Really? Have you found anything?
                    case 0:
                        Id = 60;
                        return false;
                }
                return true;
            case 60:
                // $script:1010140307011478$ 
                // - I have actually. <b>New ingredients.</b>
                // $script:1010140307011479$ 
                // - This place is littered with ingredients Maple World has never seen before!
                // $script:1010140307011480$ 
                // - When I integrate them into my menu, it'll blow people's minds. You should stop by my restaurant some time.
                switch (selection) {
                    // $script:0111224807012689$
                    // - I'll definitely pay you a visit.
                    case 0:
                        Id = 70;
                        return false;
                }
                return true;
            case 70:
                // $script:0111224807012690$ 
                // - Cool.
                return true;
            default:
                return true;
        }
    }
}
