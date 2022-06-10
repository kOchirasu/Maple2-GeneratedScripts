using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001607: Asimov
/// </summary>
public class _11001607 : NpcScript {
    internal _11001607(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006095$ 
                // - You're here.
                return true;
            case 10:
                // $script:0515180307006144$ 
                // - We've joined forces under the banner of the Starlight Expedition. I only hope we can achieve what we've set out to do. 
                return true;
            default:
                return true;
        }
    }
}
