using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000732: Shadow Tombstone
/// </summary>
public class _11000732 : NpcScript {
    internal _11000732(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000963$ 
                // - <font color="#909090">(Someone left a message.)</font>
                return true;
            case 10:
                // $script:0831180610000968$ 
                // - <font color="#909090">(There's dark energy billowing and swirling all around this tombstone! It's making it impossible to read the message.)</font>
                return true;
            default:
                return true;
        }
    }
}