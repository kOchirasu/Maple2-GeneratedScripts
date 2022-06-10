using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003102: SwolePatrol Guild Leader
/// </summary>
public class _11003102 : NpcScript {
    internal _11003102(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0119135307007835$ 
                // - Hm, you look like you could use some exercise. 
                return true;
            case 30:
                // $script:0119135307007838$ 
                // - Isn't it time you got buff? I'd invite you to my SwolePatrol guild but we don't have any openings.  
                switch (selection) {
                    // $script:0119135307007839$
                    // - I totally want to join your guild!
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0119135307007840$
                    // - Not really my scene, but thanks.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0119135307007841$ 
                // - What's wrong, got fries in your ears? Just kidding, but for real we're full. You're gonna have to find another guild to pump you up. 
                return true;
            case 32:
                // $script:0119135307007842$ 
                // - Oh, really? I have a feeling you'll be changing your mind sometime soon.  
                return true;
            default:
                return true;
        }
    }
}
