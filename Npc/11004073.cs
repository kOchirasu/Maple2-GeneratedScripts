using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004073: Fire Dragon Remains
/// </summary>
public class _11004073 : NpcScript {
    internal _11004073(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010185$ 
                // - <font color="#909090">(These are the remains of a dragon. They appear to be very old.)</font> 
                return true;
            case 10:
                // $script:0619202207010186$ 
                // - <font color="#909090">(These are the remains of a dragon. They appear to be very old.)</font> 
                // $script:0619202207010187$ 
                // - <font color="#909090">(Judging from the skeletal structure, you can tell that this was a distant cousin to the modern girant breed of dragon. It wasn't very big, but its thick jaw suggests it had a powerful bite.)</font> 
                // $script:0619202207010188$ 
                // - <font color="#909090">(You've also noticed that the fire dogs are steering clear of these remains. Did this dragon once prey on those mutts?)</font> 
                // $script:0625131207010362$ 
                // - <font color='#909090'>(One particularly long bone tells you that this dragon was male. Its 10-meter-long horn bone, to be precise.)</font> 
                // $script:0620224307010272$ 
                // - <font color="#909090">(As you examine the snout of the skull, you note a lack of flame canals present in the dragons of today. While it was obviously flame resistant, this dragon did not actually breathe fire.)</font> 
                return true;
            default:
                return true;
        }
    }
}
