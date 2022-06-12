using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004468: Rotala
/// </summary>
public class _11004468 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012113$
    // - This is a placeholder line.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012114$
                // - This is a placeholder line.
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
