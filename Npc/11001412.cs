using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001412: Sumsum
/// </summary>
public class _11001412 : NpcScript {
    internal _11001412(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217205907005409$ 
                // - So... much... pain...
                return true;
            case 40:
                // $script:1222203907005501$ 
                // - C-can't... talk... Too... busy... pain...
                switch (selection) {
                    // $script:1222203907005502$
                    // - Where does it hurt?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1222203907005503$ 
                // - Leave me alone... you dummy... I need to rest...
                switch (selection) {
                    // $script:1222203907005504$
                    // - Hey, I'm just trying to help!
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1222203907005505$ 
                // - G-go away... I don't want... your help... 
                return true;
            default:
                return true;
        }
    }
}
