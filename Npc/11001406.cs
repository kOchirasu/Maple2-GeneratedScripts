using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001406: Gree
/// </summary>
public class _11001406 : NpcScript {
    internal _11001406(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217205907005403$ 
                // - You've got guts, walking around a place like this.
                return true;
            case 40:
                // $script:1222203907005471$ 
                // - Go away! We're on a mission!!
                switch (selection) {
                    // $script:1222203907005472$
                    // - You're awfully excited for someone on a mission.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1222203907005473$ 
                // - We aren't playing, if that's what you're trying to say! We don't get to play all day like you! We're on a very, very important <i>training</i> mission!!
                return true;
            default:
                return true;
        }
    }
}
