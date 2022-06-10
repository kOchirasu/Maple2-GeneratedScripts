using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001467: Morak
/// </summary>
public class _11001467 : NpcScript {
    internal _11001467(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1223035407005528$ 
                // - Let's get to work.
                return true;
            case 30:
                // $script:1223035407005531$ 
                // - We have a saying in the construction industry: safety first. That means that it's none of my business if you do something stupid and get hurt!
                return true;
            default:
                return true;
        }
    }
}
