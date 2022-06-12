using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000327: Natalie
/// </summary>
public class _11000327 : NpcScript {
    protected override int First() {
        return 70;
    }

    // Select 0:
    // $script:0831180407001330$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (60, 0):
                // $script:0820145207008892$
                // - Everything in this world has a purpose and a story to tell.
                return -1;
            case (70, 0):
                // $script:0502125007014664$
                // - How can I help you?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (60, 0) => NpcTalkButton.Close,
            (70, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
