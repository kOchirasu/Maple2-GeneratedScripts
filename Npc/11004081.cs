using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004081: Strange Tombstone
/// </summary>
public class _11004081 : NpcScript {
    internal _11004081(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010249$ 
                // - <font color="#909090">(You faintly make out the cries of a woman. She somehow sounds far away and close at the same time.)</font> 
                return true;
            case 10:
                // $script:0619202207010250$ 
                // - <font color="#909090">(You faintly make out the cries of a woman. She somehow sounds far away and close at the same time.)</font> 
                // $script:0619202207010251$ 
                // - My child... My child... Where are you...? 
                // $script:0619202207010252$ 
                // - Come back to me... Come out of the cold... Your mama is waiting... 
                return true;
            default:
                return true;
        }
    }
}
