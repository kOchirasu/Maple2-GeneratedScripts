using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004535: Barricade Patrolman
/// </summary>
public class _11004535 : NpcScript {
    internal _11004535(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0104170807012603$ 
                // - I'm sick of fighting! Is there no end to them?! <b>Oh...!</b> Hello, $male:Sir,female:Ma'am$! I didn't see you there! 
                return true;
            case 10:
                // $script:0104170807012604$ 
                // - I'm sick of fighting! Is there no end to them?! <b>Oh...!</b> Hello, $male:Sir,female:Ma'am$! I didn't see you there! 
                // $script:0104170807012605$ 
                // - This is the biggest road to and from $map:02020041$. Maybe that's why the enemy keeps hammering us here. 
                return true;
            default:
                return true;
        }
    }
}
