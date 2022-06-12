using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004144: Iggy
/// </summary>
public class _11004144 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010559$
    // - Wanna split a nice glass of milk?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010560$
                // - Hey $male:mister,female:lady$, want to play hide-and-seek?
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
