using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000297: Quinny
/// </summary>
public class _11000297 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:0831180407001181$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407001184$
                // - I like $map:02000023$. All the trees and fairies are so pretty.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
