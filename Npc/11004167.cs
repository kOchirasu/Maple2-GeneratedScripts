using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004167: Frey
/// </summary>
public class _11004167 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010589$
    // - Is there something I can help you with?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010590$
                // - The Royal Guard protects the Empress and all of $map:02000001$. That is why we must never allow our skills to dull. So long as there are threats to peace in this world, we will not rest.
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
