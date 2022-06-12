using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000172: Mikey
/// </summary>
public class _11000172 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407000719$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407000722$
                // - This is my first job. That might not seem like a big deal, but I'm proud to be a $map:02000064$ guard. I take my responsibility to the people of $map:02000064$ very seriously.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
