using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004489: Leppens
/// </summary>
public class _11004489 : NpcScript {
    internal _11004489(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012303$ 
                // - Oh, hello. You must be here for my report. I'm afraid it's not very good... 
                return true;
            case 10:
                // $script:1227192907012304$ 
                // - Oh, hello. You must be here for my report. I'm afraid it's not very good... 
                switch (selection) {
                    // $script:1227192907012305$
                    // - Something wrong?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012306$ 
                // - I'm looking into the soil contamination that started spreading around here not too long ago. 
                // $script:1227192907012307$ 
                // - What do you know about the mechanical monster that roams this area? 
                switch (selection) {
                    // $script:1227192907012308$
                    // - I know all about it!
                    case 0:
                        Id = 12;
                        return false;
                    // $script:1227192907012309$
                    // - Not a whole lot.
                    case 1:
                        Id = 13;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012313$ 
                // - Then you're aware of how big a problem Gigantica is for us. 
                // $script:1227192907012314$ 
                // - Wherever Gigantica appears, the soil becomes tainted. We've actually had to abandoned a camp because the toxins got so bad! 
                // $script:1227192907012315$ 
                // - That's why I'm needed. If I can analyze the contamination, we may be able to counteract it—or, at the very least, predict where Gigantica will go next. 
                return true;
            case 13:
                // $script:1227192907012310$ 
                // - Really? You must not read the crew newsletter. Our efforts to explore Kritias have been hindered by this giant robotic worm. We call it Gigantica. 
                // $script:1227192907012311$ 
                // - Wherever Gigantica appears, the soil becomes tainted. We've actually had to abandon a camp because the toxins got so bad! 
                // $script:1227192907012312$ 
                // - That's why I'm needed. If I can analyze the contamination, we may be able to counteract it—or, at the very least, predict where Gigantica will go next. 
                return true;
            default:
                return true;
        }
    }
}
