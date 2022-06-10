using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000555: Shadow Tombstone
/// </summary>
public class _11000555 : NpcScript {
    internal _11000555(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000801$ 
                // - <font color="#909090">(Someone left a message.)</font>
                return true;
            case 10:
                // $script:0831180610000806$ 
                // - <font color="#909090">(There's dark energy billowing and swirling all around this tombstone! It's making it impossible to read the message.)</font>
                return true;
            default:
                return true;
        }
    }
}
