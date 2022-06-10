using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001344: Jimmy
/// </summary>
public class _11001344 : NpcScript {
    internal _11001344(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005298$ 
                // - What seems to be the problem? 
                return true;
            case 30:
                // $script:1217012607005301$ 
                // - The impossible happened. Some prisoners escaped! No one has ever escaped from Alikar before! If I don't catch them, I'm through as an officer! 
                return true;
            default:
                return true;
        }
    }
}
