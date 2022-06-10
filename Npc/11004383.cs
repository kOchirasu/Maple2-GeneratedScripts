using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004383: Judy
/// </summary>
public class _11004383 : NpcScript {
    internal _11004383(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011809$ 
                // - What kinda presents do you think Santa is bringing this year?
                return true;
            case 10:
                // $script:1109213607011810$ 
                // - What kinda presents do you think Santa is bringing this year?
                switch (selection) {
                    // $script:1109213607011811$
                    // - Do you think Santa is... real?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109213607011812$ 
                // - Seriously? You're gonna come to a festive place like this and ask THAT?
                switch (selection) {
                    // $script:1109213607011813$
                    // - I... well...
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109213607011814$ 
                // - Hey, I know the truth, but if I admit it I might get fewer presents. So yeah, go Santa!
                return true;
            default:
                return true;
        }
    }
}
