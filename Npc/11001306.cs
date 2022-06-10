using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001306: Livanda
/// </summary>
public class _11001306 : NpcScript {
    internal _11001306(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005025$ 
                // - Are you here for my father? 
                return true;
            case 40:
                // $script:1227194507005647$ 
                // - Dad's a thoughtful and affection man, if you get to know him.
                // $script:1227194507005648$ 
                // - There's more to him than he lets on.
                //   <font color="#909090">(There are tears in her eyes.)</font>
                switch (selection) {
                    // $script:1227194507005649$
                    // - Are you okay?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1227194507005650$ 
                // - I'll be okay...
                return true;
            default:
                return true;
        }
    }
}
