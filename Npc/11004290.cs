using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004290: Plutino
/// </summary>
public class _11004290 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0921211107011342$
    // - Hello. How can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0921211107011343$
                // - Welcome to our fine hotel.
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
