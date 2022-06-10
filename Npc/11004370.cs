using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004370: Claus
/// </summary>
public class _11004370 : NpcScript {
    internal _11004370(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011783$ 
                // - If you're looking for a classic holiday tree, go evergreen or go home. 
                return true;
            case 10:
                // $script:1109213607011784$ 
                // - If you're looking for a classic holiday tree, go evergreen or go home. 
                switch (selection) {
                    // $script:1120173007011855$
                    // - Ooh, an evergreen?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1120173007011856$ 
                // - There's nothing quite like it! Tall, bushy, and wonderfully scented... And if you're looking for the most beautiful tree, you'd need to get a Korean fir tree. 
                switch (selection) {
                    // $script:1120173007011857$
                    // - The Korean fir tree, you say? Hmm...
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1120173007011858$ 
                // - It grows on Mount Halla, and it's simply divine. A shame they're becoming harder to find these days. Climate change, you know. 
                return true;
            default:
                return true;
        }
    }
}
