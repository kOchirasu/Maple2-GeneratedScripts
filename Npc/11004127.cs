using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004127: Veteran Guard
/// </summary>
public class _11004127 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0720130407010497$
    // - Hmph... To think I'd be stationed in a place like this in my twilight years...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0720130407010498$
                // - So... tired... When's the next shift change?
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
