using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004070: Moonlight Wolf Statue
/// </summary>
public class _11004070 : NpcScript {
    internal _11004070(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010151$ 
                // - <font color="#909090">(This statue marks the final resting place of a great warrior from Perion.)</font> 
                return true;
            case 10:
                // $script:0619202207010152$ 
                // - <font color="#909090">(This statue marks the final resting place of a great warrior from Perion.)</font> 
                // $script:0619202207010153$ 
                // - <i>Even on the darkest night, the great Guardian of Wolfclaw Canyon fought without a hint of fear in his heart.</i> 
                // $script:0619202207010154$ 
                // - <i>Oh, brave warrior of Perion! Death is not the end. Though you are no longer in this world, your heart will be with the tribes always.</i> 
                return true;
            default:
                return true;
        }
    }
}
