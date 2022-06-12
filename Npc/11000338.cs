using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000338: Mendel
/// </summary>
public class _11000338 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407001356$
    // - How can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001357$
                // - How do you think the hotel was built on this cliff? Aren't you curious? 
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
