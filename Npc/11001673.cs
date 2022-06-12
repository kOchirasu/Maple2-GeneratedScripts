using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001673: Tinchai
/// </summary>
public class _11001673 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0711210007006723$
    // - Hah... I can barely breathe...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006898$
                // - Now isn't a great time to talk!
                switch (selection) {
                    // $script:0727223007006899$
                    // - What are these things?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006900$
                // - Whatever they are, they aren't good. Let's focus less on what they are and more on how to stop them.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
