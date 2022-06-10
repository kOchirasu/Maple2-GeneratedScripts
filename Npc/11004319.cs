using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004319: Mika
/// </summary>
public class _11004319 : NpcScript {
    internal _11004319(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1102172107011621$ 
                // - I've got a bad feeling... 
                return true;
            case 20:
                // $script:1010140307011441$ 
                // - I've got a bad feeling... 
                return true;
            case 10:
                // $script:1102172107011622$ 
                // - I sense draconic power... Did I finally find them? 
                return true;
            case 30:
                // $script:1010140307011442$ 
                // - Oh, it's you! 
                // $script:1010140307011443$ 
                // - It's been a while! What're you doing here? 
                switch (selection) {
                    // $script:1010140307011444$
                    // - What are you doing here?
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:1010140307011445$ 
                // - A few days ago I sensed an unusual energy coming from this place, so I came to investigate. 
                switch (selection) {
                    // $script:1010140307011446$
                    // - Did you find anything?
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:1010140307011447$ 
                // - Did I ever! As soon as I arrived, I felt it—that familiar aura... The traces of dragons! 
                // $script:1010140307011448$ 
                // - There's no question about it, dragons once lived in this land! I got to thinking that maybe they were related to the dark dragons that Biset told me about. 
                // $script:1010141507011602$ 
                // - Now I'm just waiting for my next big clue. 
                switch (selection) {
                    // $script:0111224807012687$
                    // - Well, good luck!
                    case 0:
                        Id = 60;
                        return false;
                }
                return true;
            case 60:
                // $script:0111224807012688$ 
                // - Thank you! 
                return true;
            default:
                return true;
        }
    }
}
