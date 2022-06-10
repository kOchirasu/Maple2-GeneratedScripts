using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003097: SwagWagon Guild Leader
/// </summary>
public class _11003097 : NpcScript {
    internal _11003097(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0119135307007815$ 
                // - Yo, what's up?
                return true;
            case 30:
                // $script:0119135307007818$ 
                // - Yo, you looking for a guild? This is the Swag Wagon, a crew of hip-hop dancers.
                switch (selection) {
                    // $script:0119135307007819$
                    // - I totally want to join your guild!
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0119135307007820$
                    // - Not really my scene, but thanks.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0119135307007821$ 
                // - I bet you do, but we're full up. You might be able to find another crew, or start your own. Don't expect to compete with us though, heh. 
                return true;
            case 32:
                // $script:0119135307007822$ 
                // - I wasn't... Uhh, okay, whatever. 
                return true;
            default:
                return true;
        }
    }
}
