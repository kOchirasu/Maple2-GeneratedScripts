using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004157: Mr. Buns
/// </summary>
public class _11004157 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010585$
    // - Meow!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010586$
                // - Nom nom nom nom!
                //   <font color="#909090">(He flops his ears joyfully.)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
