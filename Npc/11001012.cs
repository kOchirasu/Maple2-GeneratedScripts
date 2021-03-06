using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001012: Langley
/// </summary>
public class _11001012 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003454$
    // - Hello.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003457$
                // - I'm sure you heard that time stopped here in Ludibrium. Now I don't have to worry about getting old, as long as I stay here.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
