using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004462: Safehold Guardsman
/// </summary>
public class _11004462 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012077$
    // - All clear!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012078$
                // - All clear!
                return 10;
            case (10, 1):
                // $script:1227192907012079$
                // - We're doing our best to keep $map:02020041$ safe!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
