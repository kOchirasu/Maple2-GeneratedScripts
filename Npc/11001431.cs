using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001431: Ruche
/// </summary>
public class _11001431 : NpcScript {
    internal _11001431(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217205907005428$ 
                // - ...?
                return true;
            case 40:
                // $script:1222203907005516$ 
                // - ...
                switch (selection) {
                    // $script:1222203907005517$
                    // - I heard you talk!
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1222203907005518$ 
                // - <font color="#909090">($npcName:11001431[gender:0]$ tilts his head.)</font>
                switch (selection) {
                    // $script:1222203907005519$
                    // - Maybe I'm hearing things...
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1222203907005520$ 
                // - ...Heh.
                //   <font color="#909090">(Did $npcName:11001431[gender:0]$ just giggle...?)</font>
                return true;
            default:
                return true;
        }
    }
}
