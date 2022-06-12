using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004137: Mysterious Bladesman
/// </summary>
public class _11004137 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0730132107010539$
    // - Forget it.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0730132107010540$
                // - This is nothing.
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
